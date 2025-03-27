import React, { useState, useEffect } from "react";
import SelectDestination from "./steps/SelectDestination";
import SelectTransport from "./steps/SelectTransport";
import SelectActivities from "./steps/SelectActivities";
import SelectBudget from "./steps/SelectBudget";
import Summary from "./steps/Summary";
import NavButtons from "../../components/TripPlanner/NavButtons";

const TripPlanner = () => {
  const [step, setStep] = useState(0);
  const [submitReady, setSubmitReady] = useState(false);
  const [tripData, setTripData] = useState({
    destination: "",
    transport: "",
    activities: [],
    budget: 0,
  });

  const pageDisplay = () => {
    switch (step) {
      case 0:
        return <SelectDestination tripData={tripData} setTripData={setTripData}/>;
      case 1:
        return <SelectTransport tripData={tripData} setTripData={setTripData}/>;
      case 2:
        return <SelectActivities tripData={tripData} setTripData={setTripData}/>;
      case 3:
        return <SelectBudget tripData={tripData} setTripData={setTripData}/>;
      case 4:
        return <Summary tripData={tripData}/>; 
      default:
        break;
    }
  }

  useEffect(() => {
    setSubmitReady(step === 4);
  }, [step]);

  return (
    <div className="px-5 mt-10 w-1/2">
      <h2 className="font-bold text-3xl">Dinos cómo quieres viajar</h2>
      <p className="mt-3 text-gray-500 text-xl">
        GreenTrip Planner generará un itinerario según tus preferencias.
      </p>

      <div className="mt-10">
        {pageDisplay()}
      </div>

      <NavButtons
        submitReady={submitReady}
        disabledNext={step == tripData.length - 1}
        disabledBack={step == 0}
        onBack={() => {
          setStep((currStep) => currStep - 1);
        }}
        onNext={() => {
          setStep((currStep) => currStep + 1);
        }}
      />
    </div>
  );
};

export default TripPlanner;
