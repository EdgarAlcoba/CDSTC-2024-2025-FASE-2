import React, { useState, useEffect } from "react";
import SelectDestination from "./steps/SelectDestination";
import SelectTransport from "./steps/SelectTransport";
import SelectActivities from "./steps/SelectActivities";
import SelectBudget from "./steps/SelectBudget";
import Summary from "./steps/Summary";
import NavButtons from "../../components/TripPlanner/NavButtons";
import { Link } from 'react-router-dom';
import { Snackbar } from "@mui/material";
import Alert from '@mui/material/Alert';

const TripPlanner = () => {
  const [step, setStep] = useState(0);
  const [submitReady, setSubmitReady] = useState(false);
  const [snackbarOpen, setSnackbarOpen] = useState(false);
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

  const onGenerateTrip = () => {
    if (tripData.destination === "" || tripData.transport === "" || tripData.activities.length === 0 || tripData.budget === 0) {
      setSnackbarOpen(true);
      return;
    }
  
    console.log(tripData);
  };
  

  useEffect(() => {
    setSubmitReady(step === Object.keys(tripData).length);
  }, [step]);

  const handleSnackbarClose = () => {
    setSnackbarOpen(false);
  }

  return (
    <div className="bg-gray-100 min-h-screen p-5">

        <div className="">
            <div className="flex justify-between">
                <h2 className="font-bold text-3xl">Dinos cómo quieres viajar</h2>
                <Link to="/">
                    <button
                    className={"px-6 py-2 bg-gray-300 text-gray-700 rounded-lg hover:bg-gray-400 focus:outline-none"}>
                    Salir
                    </button>
                </Link>
            </div>
            <p className="mt-3 text-gray-500 text-xl">
                GreenTrip Planner generará un itinerario según tus preferencias.
            </p>
        </div>

        <div className="flex flex-col min-h-screen">
            <div className="flex-grow flex justify-center items-center">
                {pageDisplay()}
            </div>

            <div className="mb-28">
                <NavButtons
                    submitReady={submitReady}
                    disabledNext={step > Object.keys(tripData).length}
                    disabledBack={step == 0}
                    onBack={() => {
                    setStep((currStep) => currStep - 1);
                    }}
                    onNext={() => {
                      if (step < Object.keys(tripData).length) {
                        setStep((currStep) => currStep + 1);
                      } else {
                        onGenerateTrip();
                      }
                    }}
                />
              </div>
          </div>

          <Snackbar open={snackbarOpen} autoHideDuration={6000} onClose={handleSnackbarClose}>
            <Alert
              onClose={handleSnackbarClose}
              severity="error"
              variant="filled"
              sx={{ width: '100%' }}
            >
              Rellena todos los campos antes!
            </Alert>
          </Snackbar>

    </div>
  );
};

export default TripPlanner;
