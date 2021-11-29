from abc import abstractmethod, ABC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(ABC):

    @abstractmethod
    def open_page(self, driver: WebDriver) -> None:
        """
        Abstract methods to open page. Implementation will be in derived class
        Args:
            driver: WebDriver
        Returns: None
        """
        raise NotImplementedError

    @abstractmethod
    def close_page(self, driver: WebDriver) -> None:
        """
        Abstract methods to close page. Implementation will be in derived class
        Args:
            driver: WebDriver
        Returns: None
        """
        raise NotImplementedError

    @abstractmethod
    def verify_page(self, driver: WebDriver) -> None:
        """
        Abstract methods to verify page. Implementation will be in derived class
        Args:
            driver: WebDriver
        Returns: None
        """
        raise NotImplementedError
