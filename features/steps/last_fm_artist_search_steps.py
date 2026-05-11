from behave import given, when, then, Then
from selenium import webdriver
from pages.last_fm_landing_page import LastFmLandingPage
from pages.last_fm_results_page import LastFmResultsPage
from pages.last_fm_artist_page import LastFmArtistPage

@given('el usuario se encuentra en last.fm')
def step_landing_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.last.fm/")
    context.lastfm_landing = LastFmLandingPage(context.driver)


@when ('el usuario busca al artista "{artist_name}"')
def step_search_artist(context, artist_name):
   context.lastfm_landing.search_artist(artist_name)
   context.artist_name = artist_name
   context.lastfm_results = LastFmResultsPage(context.driver)


@when('navega al tab de artistas y selecciona el primer resultado')
def step_select_first_artist_result(context):
    context.lastfm_results.open_artist_page(context.artist_name)
    context.lastfm_artist = LastFmArtistPage(context.driver)


@Then('la fecha de su ultimo lanzamiento debe ser "{release_date}"')
def step_validate_date(context,release_date):
    actual = context.lastfm_artist.get_lastest_release_date()
    assert actual == release_date, f"Fecha de ultimo lanzamiento invalida: {actual}"