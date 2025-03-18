from flask import Flask, request

app = Flask(__name__)

@app.route('/<date>/<month>')
def zodiac(date,month):
    zodiac_sign = ''
    date = int(date)
    month = int(month)
    if month == 1:
        if date >= 20:
            zodiac_sign = 'Aquarius'
        else:
            zodiac_sign = 'Capricorn'
    elif month == 2:
        if date <= 18:
            zodiac_sign = 'Aquarius'
        else:
            zordiac_sign = 'Pisces'
    elif month == 3:
        if date<=20:
            zodiac_sign = 'Pisces'
        else:
            zordiac_sign = 'Aries'                
    elif month == 4:
        if date<=19:
            zodiac_sign = 'Aries'
        else:
            zordiac_sign = 'Taurus'
    elif month == 5:    
        if date<=20:
            zodiac_sign = 'Taurus'
        else:
            zordiac_sign = 'Gemini'
    elif month == 6:
        if date<=20:
            zodiac_sign = 'Gemini'
        else:
            zordiac_sign = 'Cancer'
    elif month == 7:
        if date<=22:
            zodiac_sign = 'Cancer'
        else:
            zordiac_sign = 'Leo'
    elif month == 8:
        if date<=22:
            zodiac_sign = 'Leo'
        else:
            zordiac_sign = 'Virgo'
    elif month == 9:
        if date<=22:
            zodiac_sign = 'Virgo'
        else:
            zordiac_sign = 'Libra'
    elif month == 10:
        if date<=22:
            zodiac_sign = 'Libra'
        else:
            zordiac_sign = 'Scorpion'
    elif month == 11:
        if date<=21:
            zodiac_sign = 'Scorpion'
        else:
            zordiac_sign = 'Sagittarius'
    elif month == 12:
        if date<=21:
            zodiac_sign = 'Sagittarius'
        else:
            zordiac_sign = 'Capricorn'
    else:
        zodiac_sign = 'Invalid'

    return     { 
                 'date': date,
                 'month': month,
                 'zordiac sign': zordiac_sign
               }

if __name__ == '__main__':
    app.run(debug=True,port=5000)