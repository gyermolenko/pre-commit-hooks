import astpath


def main():
    # Taken from tweet by Chase Stevens
    # https://twitter.com/hchasestevens/status/1015237280481665025
    search_path = "//Assign[targets/Name/@id = following-sibling::*[1][name(.) = 'If']/test/Name/@id]"

    found = astpath.search('.', search_path, print_matches=True, after_context=1)
    return len(found)


if __name__ == "__main__":
    exit(main())
