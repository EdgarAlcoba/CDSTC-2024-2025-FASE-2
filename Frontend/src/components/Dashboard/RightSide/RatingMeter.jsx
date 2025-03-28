import React, {useEffect} from "react";
import { Gauge, gaugeClasses } from '@mui/x-charts/Gauge';
import { useDate } from "../../../hooks/DateContext";

const settings = {
  width: 200,
  height: 200,
  value: 60,
};

export default function RatingMeter() {

  const { date } = useDate();
  
  useEffect(() => {
    /* Llamadas a back y demás */
  }, [date]);

  return (
    <div className='flex flex-col items-center p-4 rounded border 
  border-stone-300'>
      <div className='p-4'>
        <h3 className='text-base font-normal text-gray-500'>Sustainability Index</h3>
      </div>
      <div className=''>
        <Gauge
          {...settings}
          cornerRadius="50%"
          sx={(theme) => ({
            [`& .${gaugeClasses.valueText}`]: {
              fontSize: 50,
            },
            [`& .${gaugeClasses.valueArc}`]: {
              fill: '#86efac',
            },
            [`& .${gaugeClasses.referenceArc}`]: {
              fill: '#EEEDE7',
            },
          })}
        />
      </div>
    </div>
  );
}
