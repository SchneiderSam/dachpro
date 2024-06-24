# Basic design values
country = input("Bitte wählen Sie ein Land: ")
zipcode = input("Gemeindeauswahl (PLZ): ")
terrain_elevation = input("Geländehöhe [m]: ")
building_height = input("Gebäudehöhe [m]: ")
roof_length = input("Dachlänge [m]: ")
building_length = input("Gebäudelänge [m]: ")

def get_value(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

def get_values():
    choice = input("Möchten Sie die Daten manuell (m) eingeben oder die Daten aus der Statiksoftware (s) nehmen? (m/s): ").strip().lower()

    if choice == 'm':
        snow_load_standard = get_value("Bitte geben Sie den Wert für die Lastnorm Schnee ein: ")
        climate_region = get_value("Bitte geben Sie den Wert für die Klimaregion ein: ")
        snow_zone = get_value("Bitte geben Sie den Wert für die Schneezone ein: ")
        ground_snow_load = get_value("Bitte geben Sie den Wert für die Bodenschneelast ein: ")
        wind_load_standard = get_value("Bitte geben Sie den Wert für die Windlastnorm ein: ")
        wind_zone = get_value("Bitte geben Sie den Wert für die Windzone ein: ")
        terrain_category = get_value("Bitte geben Sie den Wert für die Geländekategorie ein: ")
        basic_wind_speed = get_value("Bitte geben Sie den Wert für die Basiswindgeschwindigkeit ein: ")
        basic_velocity_pressure = get_value("Bitte geben Sie den Wert für den Basisgeschwindigkeitsdruck ein: ")
    elif choice == 's':
        snow_load_standard = climate_region = snow_zone = ground_snow_load = wind_load_standard = wind_zone = terrain_category = basic_wind_speed = basic_velocity_pressure = "Siehe Daten aus Statiksoftware"
    else:
        print("Ungültige Auswahl. Bitte wählen Sie 'm' für die manuelle Eingabe oder 's' für die Daten aus Statiksoftware.")
        return get_values()

    return snow_load_standard, climate_region, snow_zone, ground_snow_load, wind_load_standard, wind_zone, terrain_category, basic_wind_speed, basic_velocity_pressure

snow_load_standard, climate_region, snow_zone, ground_snow_load, wind_load_standard, wind_zone, terrain_category, basic_wind_speed, basic_velocity_pressure = get_values()


# Results
result = f"""
Land: {country}
Gemeindeauswahl (PLZ): {zipcode}
Geländehöhe: {terrain_elevation} m
Gebäudehöhe: {building_height} m
Dachlänge: {roof_length} m
Gebäudelänge: {building_length} m
Lastnorm Schnee: {snow_load_standard}
Klimaregion: {climate_region}
Schneezone: {snow_zone}
Bodenschneelast: {ground_snow_load}
Windlastnorm: {wind_load_standard}
Windzone: {wind_zone}
Geländekategorie: {terrain_category}
Grundwindgeschwindigkeit: {basic_wind_speed}
Grundgeschwindigkeitsdruck: {basic_velocity_pressure}
"""

print(result)
