import React from 'react'
import StatCards from './StatCards'
import GraphCards from './Charts/GraphCards'
import Map from './Map'
import RightPanel from './RightSide/RightPanel'

const Grid = () => {
  return (
    <div className='px-4 grid gap-3 grid-cols-12'>
      <StatCards />
      <GraphCards />
      <Map />
      <RightPanel />
    </div>
  )
}

export default Grid
