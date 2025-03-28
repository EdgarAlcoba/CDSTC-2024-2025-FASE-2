import React, { useEffect } from 'react'
import {useDate} from '../../hooks/DateContext'

const StatCards = () => {

  const { date } = useDate();

  useEffect(() => {
    /* Llamadas a back y demás */
  }, [date]);

  return (
    <>
      <Card
        title="Occupation"
        value="12,567"
        percentage="2.34%"
        trend="up"
        period="From Jan 1st - Jul 31st" />
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
  percentage,
  trend,
  period
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
          +{percentage} than yersterday
        </h3>
      </div>
    </div>
  </div>
}

export default StatCards
