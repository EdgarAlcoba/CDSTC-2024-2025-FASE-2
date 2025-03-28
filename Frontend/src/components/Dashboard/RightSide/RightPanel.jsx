import React from 'react'
import RatingMeter from './RatingMeter'
import VehicleCard from './VehicleCard'

const RightPanel = () => {
  return (
    <div className='flex flex-col gap-3 col-span-3 overflow-hidden rounded'>
      <RatingMeter />
      <VehicleCard />
    </div>
  )
}

export default RightPanel
