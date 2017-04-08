def city(name, country, population=''):
    """Outputs a string of the city and the country."""
    if population:
        city_address = f"{name}, {country} - {population}"
        return city_address.title()
    else:
        city_address = f"{name}, {country}"
        return city_address.title()
