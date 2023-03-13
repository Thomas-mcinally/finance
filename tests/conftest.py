import pytest
import responses


@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as rsps:
        yield rsps


@pytest.fixture
def mock_GET_yahoo_v8_finance_chart_api_30day_range(mocked_responses):
    def _mock_GET_yahoo_v8_finance_chart_api_30day_range(ticker, json_response):
        mocked_responses.get(
            f"https://query2.finance.yahoo.com/v8/finance/chart/{ticker}",
            match=[
                responses.matchers.query_param_matcher(
                    {"range": "30d", "interval": "1d"}
                ),
                responses.matchers.header_matcher({"User-Agent": "Mozilla/5.0"}),
            ],
            status=200,
            json=json_response,
        )

    return _mock_GET_yahoo_v8_finance_chart_api_30day_range

example_yahoo_api_response_30day_tsla_2023_03_13 = {
    "chart": {
        "result": [
            {
                "meta": {"currency": "USD", "symbol": "TSLA"},
                "timestamp": [
                    1675089000,
                    1675175400,
                    1675261800,
                    1675348200,
                    1675434600,
                    1675693800,
                    1675780200,
                    1675866600,
                    1675953000,
                    1676039400,  # fri 10th feb, "30 days ago"
                    1676298600,
                    1676385000,
                    1676471400,
                    1676557800,
                    1676644200,
                    1676989800,
                    1677076200,
                    1677162600,
                    1677249000,
                    1677508200,
                    1677594600,
                    1677681000,
                    1677767400,
                    1677853800,
                    1678113000,  # mon 6th mar, "7 days ago"
                    1678199400,
                    1678285800,
                    1678372200,
                    1678458600,
                    1678736998,  # mon 13th mar, "today"
                ],
                "indicators": {
                    "quote": [
                        {
                            "close": [
                                166.66000366210938,
                                173.22000122070312,
                                181.41000366210938,
                                188.27000427246094,
                                189.97999572753906,
                                194.75999450683594,
                                196.80999755859375,
                                201.2899932861328,
                                207.32000732421875,
                                196.88999938964844,  # fri 10th feb, "30 days ago"
                                194.63999938964844,
                                209.25,
                                214.24000549316406,
                                202.0399932861328,
                                208.30999755859375,
                                197.3699951171875,
                                200.86000061035156,
                                202.07000732421875,
                                196.8800048828125,
                                207.6300048828125,
                                205.7100067138672,
                                202.77000427246094,
                                190.89999389648438,
                                197.7899932861328,
                                193.80999755859375,  # mon 6th mar, "7 days ago"
                                187.7100067138672,
                                182.0,
                                172.9199981689453,
                                173.44000244140625,
                                174.951904296875,  # mon 13th mar, "today"
                            ]
                        }
                    ]
                },
            }
        ]
    }
}

example_yahoo_api_response_30day_aapl_2023_03_13 = {
    "chart": {
        "result": [
            {
                "meta": {"currency": "USD", "symbol": "AAPL"},
                "timestamp": [
                    1675089000,
                    1675175400,
                    1675261800,
                    1675348200,
                    1675434600,
                    1675693800,
                    1675780200,
                    1675866600,
                    1675953000,
                    1676039400,  # fri 10th feb, "30 days ago"
                    1676298600,
                    1676385000,
                    1676471400,
                    1676557800,
                    1676644200,
                    1676989800,
                    1677076200,
                    1677162600,
                    1677249000,
                    1677508200,
                    1677594600,
                    1677681000,
                    1677767400,
                    1677853800,
                    1678113000,  # mon 6th mar, "7 days ago"
                    1678199400,
                    1678285800,
                    1678372200,
                    1678458600,
                    1678737604,  # mon 13th mar, "today"
                ],
                "indicators": {
                    "quote": [
                        {
                            "close": [
                                143.0,
                                144.2899932861328,
                                145.42999267578125,
                                150.82000732421875,
                                154.5,
                                151.72999572753906,
                                154.64999389648438,
                                151.9199981689453,
                                150.8699951171875,
                                151.00999450683594, # fri 10th feb, "30 days ago"
                                153.85000610351562,
                                153.1999969482422,
                                155.3300018310547,
                                153.7100067138672,
                                152.5500030517578,
                                148.47999572753906,
                                148.91000366210938,
                                149.39999389648438,
                                146.7100067138672,
                                147.9199981689453,
                                147.41000366210938,
                                145.30999755859375,
                                145.91000366210938,
                                151.02999877929688,
                                153.8300018310547, # mon 6th mar, "7 days ago"
                                151.60000610351562,
                                152.8699951171875,
                                150.58999633789062,
                                148.5,
                                150.47000122070312, # current price
                            ]
                        }
                    ]
                },
            }
        ]
    }
}
