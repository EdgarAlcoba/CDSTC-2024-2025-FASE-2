import { useState } from "react"; 
import Datepicker from "react-tailwindcss-datepicker";
import { useDate } from '../../../hooks/DateContext';

const START_FROM = new Date(2019, 0, 7); // Enero es el mes 0 en JavaScript
const MIN_DATE = new Date(2019,0,7);
const MAX_DATE = new Date(2024,11,31);

const DatePicker = () => {

    const { setDate } = useDate();

    const [value, setValue] = useState({ 
        startDate: null, 
        endDate: null
    });

    const handleChange = (newValue) => {
        setValue(newValue);
        setDate(newValue); // Actualiza el estado global
    };

    return (
        <Datepicker
            useRange={false}
            startFrom={START_FROM}
            minDate={MIN_DATE}
            maxDate={MAX_DATE}
            asSingle={true}
            primaryColor={"emerald"}
            value={value} 
            onChange={handleChange}
        /> 
    );
};

export default DatePicker;
