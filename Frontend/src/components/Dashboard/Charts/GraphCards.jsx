import React from 'react'
import AreaChartCard from './AreaChartCard'

const GraphCards = () => {

  const data = [6500, 6418, 6456, 6526, 6356, 6456];
  const dates = ['01 February', '02 February', '03 February', '04 February', '05 February', '06 February', '07 February'];

  return (
    <div
    className='flex flex-col gap-3 col-span-3 overflow-hidden rounded'>
      <AreaChartCard title={'Occupation (Last week)'} variable={'Guests'} 
      percentage={'12%'} data={data} dates={dates}/>
      <AreaChartCard title={'Price/night (Last week)'} variable={'Price/night'} 
      percentage={'14%'} data={data} dates={dates}/>
    </div>
  )
}

export default GraphCards
