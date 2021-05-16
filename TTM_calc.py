import yfinance as yf


ticker_name_list = [
    "GOOG",
    "AMZN",
    "AAPL",
    "FB",
    "MSFT",
    "TSLA",
    "NVDA",
    "AMD",
    "INTC",
    "TSM",
    "JPM",
    "BAC",
    "T",
    "U",
    "NNDM",
    "Z",
    "OPEN",
    "RDFN",
    "005930.KS",
    "035420.KS",
    "035720.KS",
    "055550.KS",
    "105560.KS",
    "086790.KS",
    "316140.KS",
    "024110.KS",
    "005380.KS",
    "000270.KS",
    "066570.KS",
    "000660.KS",
    "005490.KS",
    "017670.KS",
    "003490.KS",
    "020560.KS",
    "089590.KS",

]


def main():
    with open("output.csv", "w") as fp:
        fp.write("ticker,revenue,earning,stock price,market cap\n")

        for ticker_name in ticker_name_list:
            ticker = yf.Ticker(ticker_name)
            # print(ticker.info)
            # print(ticker.quarterly_earnings)
            earning = ticker.quarterly_earnings.values
            rev = 0
            ear = 0
            for i in earning:
                rev += i[0]
                ear += i[1]

            div = 1000000
            if "KS" in ticker_name:
                div = 100000000
            rev /= div
            ear /= div
            str_val = str(ticker_name)+","
            str_val += str(rev) + ","
            str_val += str(ear) + ","
            str_val += str(ticker.info.get("regularMarketPrice")) + ","
            str_val += str(ticker.info.get("marketCap") / div)

            print(str_val)
            fp.write(str_val)
            fp.write("\n")

        fp.close()


if __name__ == "__main__":
    main()
