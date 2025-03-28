import React, {useEffect} from "react";
import { useDate } from "../../../hooks/DateContext";

const VehicleCard = () => {

  const { date } = useDate();
  
  useEffect(() => {
    /* Llamadas a back y demás */
  }, [date]);

  return (
    <div className='bg-white rounded shadow-sm p-4 md:p-6 border border-stone-300'>
      Algo aqui de sostenibilidad
    </div>
  )
}

export default VehicleCard
