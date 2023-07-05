import os
import time

import requests
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from dotenv import load_dotenv

from generator.forms import GeneratorForm
from generator.models import Lead

load_dotenv()

TEXT_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
PLACE_DETAIL_URL = "https://maps.googleapis.com/maps/api/place/details/json"


def get_places(
    location: str = None, keywords: str = None, next_page_token: str = None
) -> tuple[str, list[dict]]:
    if next_page_token:
        response = requests.get(
            TEXT_URL,
            params={
                "pagetoken": next_page_token,
                "key": os.getenv("GOOGLE_API_KEY"),
            },
        )
        return response.json().get("next_page_token"), response.json().get(
            "results"
        )

    response = requests.get(
        TEXT_URL,
        params={
            "query": f"{location} {keywords}",
            "key": os.getenv("GOOGLE_API_KEY"),
        },
    )
    return response.json().get("next_page_token"), response.json().get(
        "results"
    )


def get_place_detail_info(place_id: str) -> dict[str, str]:
    response = requests.get(
        PLACE_DETAIL_URL,
        params={
            "fields": "name,formatted_address,"
            "international_phone_number,website,geometry,rating",
            "place_id": place_id,
            "key": os.getenv("GOOGLE_API_KEY"),
            "language": "en",
        },
    )
    return response.json().get("result")


@login_required
def index(request: HttpRequest) -> HttpResponse:
    form = GeneratorForm(request.POST or None)
    leads = []

    if request.method == "POST":
        next_page_token, places = get_places(
            location=form.data.get("location"),
            keywords=form.data.get("keywords"),
        )

        while next_page_token and int(form.data.get("leads_num")) > len(
            places
        ):
            time.sleep(1)
            next_page_token, next_places = get_places(
                next_page_token=next_page_token
            )
            places.extend(next_places)

        place_ids = [
            place["place_id"]
            for place in places[: int(form.data.get("leads_num"))]
        ]
        for place_id in place_ids:
            detail_info = get_place_detail_info(place_id)
            updated_values = {
                "address": detail_info.get("formatted_address"),
                "phone": detail_info.get("international_phone_number"),
                "site_url": detail_info.get("website"),
                "rating": detail_info.get("rating"),
                "location": detail_info.get("geometry").get("location"),
            }
            lead, _ = Lead.objects.update_or_create(
                name=detail_info.get("name"),
                defaults=updated_values,
            )
            leads.append(lead)

    return render(
        request,
        template_name="index.html",
        context={"form": form, "leads": leads},
    )
