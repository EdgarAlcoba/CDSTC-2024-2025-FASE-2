import { createContext, useState, useContext } from "react";

const DateContext = createContext();

const START_FROM = new Date(2019, 0, 1);

export const DateProvider = ({ children }) => {
  const [date, setDate] = useState({ startDate: START_FROM, endDate: START_FROM });

  return (
    <DateContext.Provider value={{ date, setDate }}>
      {children}
    </DateContext.Provider>
  );
};

export const useDate = () => useContext(DateContext);
