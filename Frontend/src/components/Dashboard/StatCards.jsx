import React, { useEffect, useState } from 'react'
import {useDate} from '../../hooks/DateContext'
import api from '../../Api'

const StatCards = () => {

  const { date } = useDate();
  const [occupation, setOccupation] = useState(0);
  const [price, setPrice] = useState(0);
  const [cancellations, setCancellations] = useState(0);

  useEffect(() => {

    let formattedDate = date.startDate.toLocaleDateString('en-CA');
    api.post('/getOccupation', {
      date: formattedDate,
      city_id: 0
    })
    .then((response) => {
      setOccupation(response.data.occupations_avg_percent);
    })
    .catch((error) => {
      if (error.response) {
        console.error("Error al solicitar la ocupación:", error.response.data);
      } else {
        console.error("Error desconocido:", error.message);
      }
    });
    
    api.post('/getAveragePrice', {
      date: formattedDate,
      city_id: 0
    })
    .then((response) => {
      setPrice(response.data.average_price);
    })
    .catch((error) => {
      if (error.response) {
        console.error("Error al solicitar el precio:", error.response.data);
      } else {
        console.error("Error desconocido:", error.message);
      }
    });
    
    api.post('/getCancellations', {
      date: formattedDate,
      city_id: 0
    })
    .then((response) => {
      setCancellations(response.data.cancellations_sum);
    })
    .catch((error) => {
      if (error.response) {
        console.error("Error al solicitar las cancelaciones:", error.response.data);
      } else {
        console.error("Error desconocido:", error.message);
      }
    }); 
    
  }, [date]);

  return (
    <>
      <Card
        title="Occupation"
        value={occupation+"%"}
      />
      <Card 
        title="Avg price/night"
        value={"$"+price}
      />
      <Card 
        title="Cancellations"
        value={cancellations}
      />
    </>
  )
}

const Card = ({
  title,
  value,
  }) => {
  return <div className='col-span-4 p-4 rounded border 
  border-stone-300'>
    <div className='flex items-start 
    justify-between'>
      <div>
        <h3 className='text-stone-500 mb-2 text-base'>
          {title}
        </h3>
        <p className='text-3xl font-semibold'>{value}
        </p>
      </div>
    </div>
  </div>
}

export default StatCards
