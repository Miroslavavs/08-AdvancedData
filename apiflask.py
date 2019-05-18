{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "measurement",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[0;32m/anaconda3/lib/python3.7/site-packages/sqlalchemy/util/_collections.py\u001b[0m in \u001b[0;36m__getattr__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m    209\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 210\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_data\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    211\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mKeyError\u001b[0m: 'measurement'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-5c11e590295c>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0mBase\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mautomap_base\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     13\u001b[0m \u001b[0mBase\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprepare\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mengine\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreflect\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 14\u001b[0;31m \u001b[0mMeasurement\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBase\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclasses\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmeasurement\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     15\u001b[0m \u001b[0mStation\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBase\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclasses\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstation\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     16\u001b[0m \u001b[0msession\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mSession\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mengine\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/anaconda3/lib/python3.7/site-packages/sqlalchemy/util/_collections.py\u001b[0m in \u001b[0;36m__getattr__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m    210\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_data\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    211\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 212\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    213\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    214\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__contains__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mAttributeError\u001b[0m: measurement"
     ]
    }
   ],
   "source": [
    "import datetime as dt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "\n",
    "from flask import Flask, jsonify\n",
    "engine = create_engine(\"sqlite:///hawaii.sqlite\")\n",
    "Base = automap_base()\n",
    "Base.prepare(engine, reflect=True)\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station\n",
    "session = Session(engine)\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route(\"/\")\n",
    "def welcome():\n",
    "    return (\n",
    "        \n",
    "        f\"Available Routes:<br/>\"\n",
    "        f\"/api/v1.0/precipitation<br/>\"\n",
    "        f\"/api/v1.0/stations<br/>\"\n",
    "        f\"/api/v1.0/tobs<br/>\"\n",
    "        f\"/api/v1.0/temp/start/end\"\n",
    "    )\n",
    "\n",
    "\n",
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def precipitation():\n",
    "    \"\"\"Return the precipitation data for the last year\"\"\"\n",
    "    # Calculate the date 1 year ago from last date in database\n",
    "    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)\n",
    "\n",
    "    # Query for the date and precipitation for the last year\n",
    "    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()\n",
    "\n",
    "    # Dict with date as the key and prcp as the value\n",
    "    precip = {date: prcp for date, prcp in precipitation}\n",
    "    return jsonify(precip)\n",
    "\n",
    "\n",
    "@app.route(\"/api/v1.0/stations\")\n",
    "def stations():\n",
    "    \"\"\"Return a list of stations.\"\"\"\n",
    "    results = session.query(Station.station).all()\n",
    "\n",
    "    # Unravel results into a 1D array and convert to a list\n",
    "    stations = list(np.ravel(results))\n",
    "    return jsonify(stations)\n",
    "\n",
    "\n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
