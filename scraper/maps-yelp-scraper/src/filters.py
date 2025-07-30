def filter_businesses_without_website(businesses):
    """
    Filters out businesses that already have a website.

    Parameters:
    businesses (list): A list of business dictionaries containing details.

    Returns:
    list: A list of businesses without a website.
    """
    return [business for business in businesses if not business.get('website')]