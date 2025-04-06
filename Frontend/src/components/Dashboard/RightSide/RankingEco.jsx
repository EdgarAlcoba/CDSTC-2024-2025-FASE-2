import React, {useEffect, useState} from "react";
import { useDate } from "../../../hooks/DateContext";
import api from '../../../Api'

const RankingEco = () => {

  const { date } = useDate();
  const [hotels, setHotels] = useState([]);
  
  useEffect(() => {

    let formattedDate = date.startDate.toLocaleDateString('en-CA');
    
    api.post('/getEcoIndex', {
      date: formattedDate,
      city_id: 0
    })
    .then((response) => {
      setHotels(response.data.top_eco_hotels);
    })
    .catch((error) => {
      if (error.response) {
        console.error("Error al solicitar los hoteles:", error.response.data);
      } else {
        console.error("Error desconocido:", error.message);
      }
    });

  }, [date]);

  return (
    <div className='flex flex-col bg-white rounded shadow-sm p-4 md:p-6 border border-stone-300 h-full'>
      <h1 className="text-xl font-bold text-gray-700">Top Eco Hotels</h1>
      <div className="flex-grow">
        {hotels.length > 0 ? (
          <ul className="mt-4 space-y-2">
            {hotels.map((hotel, index) => (
              <li key={index} className="p-2 border-b border-gray-200">
                <span className="text-lg font-medium text-gray-800">{hotel.name}</span>
                <p className="text-sm text-gray-600">Eco Score: {hotel.sustainability_percent}</p>
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-gray-500 mt-4">No hay hoteles disponibles.</p>
        )}
      </div>
    </div>
  )
}

export default RankingEco
