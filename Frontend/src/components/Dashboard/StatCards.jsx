import React, { useEffect, useState } from 'react'
import {useDate} from '../../hooks/DateContext'
import api from '../../Api'

const StatCards = () => {

  const { date } = useDate();
  const [occupation, setOccupation] = useState(0);

  useEffect(() => {

    let formattedDate = date.startDate.toLocaleDateString('en-CA');
    
    fetch('http://localhost/getOccupation', {
      method: 'GET',  // 🚨 GET con body (NO estándar)
      body: JSON.stringify({
        date: formattedDate,
        city_id: 0
      }),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
    
    
  }, [date]);

  return (
    <>
      <Card
        title="Occupation"
        value={occupation+"%"}
      />
      <Card 
        title="Avg price/night"
        value="$122"
        percentage="4.55%"
        trend="down"
        period="From Jan 1st - Jul 31st"/>
      <Card 
        title="Cancellations"
        value="34"
        percentage="7%"
        trend="up"
        period="Last 30 days"/>
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
        <h3 className='text-stone-500 mb-2 text-sm'>
          {title}
        </h3>
        <p className='text-3xl font-semibold'>{value}
        </p>
        <h3 className='text-stone-500 mb-2 text-sm'>
          +{"percentage"} than yersterday
        </h3>
      </div>
    </div>
  </div>
}

export default StatCards
