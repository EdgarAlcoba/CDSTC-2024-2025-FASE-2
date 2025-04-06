import React, { useEffect, useState } from 'react'
import AreaChartCard from './AreaChartCard'
import { useDate } from "../../../hooks/DateContext";
import api from '../../../Api';

const GraphCards = () => {

  const [occupation, setOccupation] = useState([]);
  const [prices, setPrices] = useState([]);
  const [dates, setDates] = useState([]);

  const data = [6500, 6418, 6456, 6526, 6356, 6456];
  const datess = ['01 February', '02 February', '03 February', '04 February', '05 February', '06 February', '07 February'];

  const { date } = useDate();

  useEffect(() => {

    let formattedDate = date.startDate.toLocaleDateString('en-CA');

    api.post('/getOccupationLast7Days', {
      date: formattedDate,
      city_id: 0
    })
    .then((response) => {
      const dates = response.data.map(item => item.day);
      const occupation = response.data.map(item => item.occupation_rate);
      setDates(dates.reverse());
      setOccupation(occupation.reverse());
    })
    .catch((error) => {
      if (error.response) {
        console.error("Error al solicitar la ocupación:", error.response.data);
      } else {
        console.error("Error desconocido:", error.message);
      }
    });

    api.post('/getAveragePriceLast7Days', {
      date: formattedDate,
      city_id: 0
    })
    .then((response) => {
      const avg_price = response.data.map(item => item.average_night_price);
      setPrices(avg_price.reverse());
    })
    .catch((error) => {
      if (error.response) {
        console.error("Error al solicitar los precios:", error.response.data);
      } else {
        console.error("Error desconocido:", error.message);
      }
    });

  }, [date]);

  return (
    <div
    className='flex flex-col gap-3 col-span-3 rounded'>
      <AreaChartCard title={'Occupation (7 days)'} variable={'Occupation %'} 
      description={'Shows the % variation along the week'} data={occupation} dates={dates}/>
      <AreaChartCard title={'Price/night (7 days)'} variable={'Avg Price/night'} 
      description={'Shows the price variation along the week'} data={prices} dates={dates}/>
    </div>
  )
}

export default GraphCards
