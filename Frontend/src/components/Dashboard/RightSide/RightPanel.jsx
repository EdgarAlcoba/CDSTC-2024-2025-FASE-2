import React from 'react'
import RatingMeter from './RatingMeter'
import RankingEco from './RankingEco'

const RightPanel = () => {
  return (
    <div className='flex flex-col gap-3 col-span-3 overflow-hidden rounded'>
      <RatingMeter />
      <RankingEco />
    </div>
  )
}

export default RightPanel
