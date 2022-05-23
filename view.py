import model


def html_view():
    result_str = '<u>Погода сейчас в:</u> \n'
    result_str += f"{model.weather_model['city']}\n"
    result_str += f"<b>температура: {model.weather_model['temperature']} °С</b>\n"
    result_str += f"{model.weather_model['weather_description']}\n"
    result_str += f"давление {int(model.weather_model['pressure'] * 0.750062)} мм.рт.ст\n"
    result_str += f"влажность {model.weather_model['humidity']} %\n"
    result_str += f"ветер {model.weather_model['wind_direction']}, {model.weather_model['wind_speed']} м/с"
    return result_str