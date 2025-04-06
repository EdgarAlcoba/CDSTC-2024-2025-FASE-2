import React from 'react'
import TopBar from '../../components/Dashboard/Topbar/TopBar'
import Grid from '../../components/Dashboard/Grid'
import { DateProvider } from '../../hooks/DateContext'
import Navbar from '../../components/Navbar/Navbar'

const Dashboard = () => {
  return (
    <div className='bg-white rounded-lg pt-1 shadow w-full'>
      <Navbar />
      <DateProvider>
        <TopBar />
        <Grid />
      </DateProvider>
    </div>
  )
}

export default Dashboard
