import React, {useEffect} from 'react'
import DatePicker from './DatePicker'
import { useDate } from '../../../hooks/DateContext';

const TopBar = () => {

  const { date } = useDate();
    
  useEffect(() => {
    /* Llamadas a back y demás */
  }, [date]);

  return (
    <div className='border-b px-4 mb-4 mt-2 pb-4 
    border-stone-200'>
      <div className='flex items-center 
      justify-between p-0.5'>
        <div>
            <span className='text-3xl font-bold block'>
                Good morning, GreenLake!</span>
            <span className='text-s block
            text-stone-500'>{date.startDate?.toDateString()}</span>
        </div>

        <button className='flex text-sm items-center
        gap-2 bg-stone-100 transition-colors
        hover:bg-green-300 px-3 py-1.5 rounded'>
            <DatePicker />
            <span>Select a date</span>
        </button>
      </div>
    </div>
  )
}

export default TopBar
