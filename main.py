# Basic design values
country = input("Bitte wählen Sie ein Land: ")
zipcode = input("Gemeindeauswahl (PLZ): ")
terrain_elevation = input("Geländehöhe [m]: ")
building_height = input("Gebäudehöhe [m]: ")
roof_length = input("Dachlänge [m]: ")
building_length = input("Gebäudelänge [m]: ")

# Get values
def get_value(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

def get_load_values():
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
        return get_load_values()

    return snow_load_standard, climate_region, snow_zone, ground_snow_load, wind_load_standard, wind_zone, terrain_category, basic_wind_speed, basic_velocity_pressure

# PV System
def get_pv_system():
    while True:
        pv_system = input("Soll auf dem Dach eine PV-Anlage installiert werden? (j/n): ").strip().lower()
        if pv_system in ['j', 'n']:
            return pv_system
        else:
            print("Ungültige Eingabe. Bitte geben Sie 'j' (ja) oder 'n' (nein) ein.")

# PV System
def get_pv_system_details():
    pv_model_left = input("Bitte geben Sie das Modell der linken PV-Anlage ein: ")
    pv_left_distance_to_eaves = get_value("Bitte geben Sie den Abstand der linken PV-Anlage zur Traufe ein: ")
    pv_left_length = get_value("Bitte geben Sie die Länge der linken PV-Anlage ein: ")

    pv_model_right = input("Bitte geben Sie das Modell der rechten PV-Anlage ein: ")
    pv_right_distance_to_ridge = get_value("Bitte geben Sie den Abstand der rechten PV-Anlage zum First ein: ")
    pv_right_length = get_value("Bitte geben Sie die Länge der rechten PV-Anlage ein: ")

    return {
        "pv_model_left": pv_model_left,
        "pv_left_distance_to_eaves": pv_left_distance_to_eaves,
        "pv_left_length": pv_left_length,
        "pv_model_right": pv_model_right,
        "pv_right_distance_to_ridge": pv_right_distance_to_ridge,
        "pv_right_length": pv_right_length
    }

def format_pv_system_details(pv_details):
    return f"""
PV-Anlage
PV-Anlage links
Modell: {pv_details['pv_model_left']}
PV,li Abstand zur Traufe [m]: {pv_details['pv_left_distance_to_eaves']}
PV,li Länge [m]: {pv_details['pv_left_length']}

PV-Anlage rechts
Modell: {pv_details['pv_model_right']}
PV,re Abstand zum First [m]: {pv_details['pv_right_distance_to_ridge']}
PV,re Länge [m]: {pv_details['pv_right_length']} 
"""

# Maincode
snow_load_standard, climate_region, snow_zone, ground_snow_load, wind_load_standard, wind_zone, terrain_category, basic_wind_speed, basic_velocity_pressure = get_load_values()
pv_system = get_pv_system()

if pv_system == 'j':
    pv_details = get_pv_system_details()
    pv_result = format_pv_system_details(pv_details)
else:
    pv_result = "Es ist keine PV-Anlage geplant.\n"

result = f"""
Konstruktions Grundwerte
Land: {country}
Gemeindeauswahl (PLZ): {zipcode}
Geländehöhe: {terrain_elevation} m
Gebäudehöhe: {building_height} m
Dachlänge: {roof_length} m
Gebäudelänge: {building_length} m

Schnee Grundwerte
Lastnorm Schnee: {snow_load_standard}
Klimaregion: {climate_region}
Schneezone: {snow_zone}
Bodenschneelast: {ground_snow_load}

Wind Grundwerte
Windlastnorm: {wind_load_standard}
Windzone: {wind_zone}
Geländekategorie: {terrain_category}
Grundwindgeschwindigkeit: {basic_wind_speed}
Grundgeschwindigkeitsdruck: {basic_velocity_pressure}

{pv_result}
"""

print(result)
