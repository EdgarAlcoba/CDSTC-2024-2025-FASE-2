import React, {useEffect, useState} from "react";
import { Gauge, gaugeClasses } from '@mui/x-charts/Gauge';
import { useDate } from "../../../hooks/DateContext";
import api from '../../../Api'

export default function RatingMeter() {

  const { date } = useDate();
  const [ecoIndex, setEcoIndex] = useState(0);
  
  useEffect(() => {

    let formattedDate = date.startDate.toLocaleDateString('en-CA');
    
    api.post('/getEcoIndex', {
      date: formattedDate,
      city_id: 0
    })
    .then((response) => {
      setEcoIndex(response.data.average_eco_index);
    })
    .catch((error) => {
      if (error.response) {
        console.error("Error al solicitar el EcoIndex:", error.response.data);
      } else {
        console.error("Error desconocido:", error.message);
      }
    });

  }, [date]);

  const settings = {
    width: 200,
    height: 200,
    value: ecoIndex,
  };

  return (
    <div className='flex flex-col items-center p-4 rounded border 
  border-stone-300'>
      <div className='p-4'>
        <h3 className='text-xl font-bold text-gray-700'>Sustainability Index</h3>
      </div>
      <div className=''>
        <Gauge
          {...settings}
          cornerRadius="50%"
          sx={(theme) => ({
            [`& .${gaugeClasses.valueText}`]: {
              fontSize: 40,
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
