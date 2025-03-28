import React from 'react'
import TopBar from '../../components/Dashboard/Topbar/TopBar'
import Grid from '../../components/Dashboard/Grid'
import { DateProvider } from '../../hooks/DateContext'

const Dashboard = () => {
  return (
    <div className='bg-white rounded-lg 
    pb-4 shadow w-full'>
      <DateProvider>
        <TopBar />
        <Grid />
      </DateProvider>
    </div>
  )
}

export default Dashboard
