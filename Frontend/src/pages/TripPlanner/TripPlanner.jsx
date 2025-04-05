import React, { useState, useEffect } from "react";
import SelectDestination from "./steps/SelectDestination";
import SelectTransport from "./steps/SelectTransport";
import SelectActivities from "./steps/SelectActivities";
import SelectBudget from "./steps/SelectBudget";
import Summary from "./steps/Summary";
import NavButtons from "../../components/TripPlanner/NavButtons";
import { Snackbar } from "@mui/material";
import Alert from '@mui/material/Alert';
import NavBar from '../../components/Navbar/Navbar'
import SelectDays from "./steps/SelectDays";

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
        return <SelectDays tripData={tripData} setTripData={setTripData}/>;
      case 2:
        return <SelectTransport tripData={tripData} setTripData={setTripData}/>;    
      case 3:
        return <SelectActivities tripData={tripData} setTripData={setTripData}/>;  
      case 4:
        return <SelectBudget tripData={tripData} setTripData={setTripData}/>;   
      case 5:
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
    <div className="bg-white min-h-screen">
      <NavBar />

        <div className="mt-5 bg-gray-100 py-5 rounded-lg mx-5">
            <div className="flex justify-center">
                <h2 className="font-semibold text-3xl">¿Cómo te imaginas tu próximo viaje?</h2>
            </div>
            <div className="flex justify-center">
              <p className="mt-3 text-gray-500">
              Nuestro asistente potenciado por IA te ayudará a planearlo en detalle.
              </p>
            </div>
        </div>

        <div className="flex flex-col justify-center items-center min-h-[70vh] mt-5">
            <div className="flex-grow flex flex-col justify-center items-center">
                {pageDisplay()}
              </div>

              <div className="mb-10">
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
              Fill in all the fields!
            </Alert>
          </Snackbar>

    </div>
  );
};

export default TripPlanner;
