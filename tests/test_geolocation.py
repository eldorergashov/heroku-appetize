import allure
import pytest

from services.herokuapp.pages.geolocation import GeoLocation
from utility.enumerators import ENV


class TestGeoLocation:

    @allure.feature('GeoLocation Page')
    @allure.title("Testing WhereAmI functionality in GeoLocation.")
    @allure.testcase("https://spoton.testrail.io/index.php?/cases/view/999903", 'Test Case Link')
    @pytest.mark.C999903  # TestRail ID
    @pytest.mark.smoke
    @pytest.mark.parametrize("environment", [ENV.PROD])
    def test_geolocation_where_am_i(self, driver, environment):
        geo_location_page = GeoLocation(env=environment)
        geo_location_page.open_page(driver)
        geo_location_page.verify_page(driver)
        geo_location_page.click_where_am_i(driver)
        latitude = geo_location_page.get_latitude_text(driver)
        longitude = geo_location_page.get_longitude_text(driver)
        assert latitude and longitude is not None
        print('My geolocation is:\n' +
        'latitude: ' + latitude + '\n'
        'longitude: ' + longitude)
