import { TextField } from "@mui/material";
import React, { useState } from "react";

const SelectConsiderations = ({ tripData, setTripData }) => {
    const handleConsiderationsChange = (event) => {
        const newConsiderations = event.target.value;
        setTripData((prevData) => ({
            ...prevData,
            considerations: newConsiderations,
        }));
    };

    return (
        <div className="p-5 bg-white rounded-xl shadow-md">
            <h2 className="text-xl font-semibold text-gray-800">🖊️ Peticiones especiales</h2>

            <div className="flex gap-3 mt-4 flex-wrap">
                <TextField
                    label="Peticiones"
                    multiline
                    maxRows={10}
                    fullWidth
                    variant="outlined"
                    sx={{ minWidth: '40vw'}}
                    value={tripData.considerations}
                    onChange={handleConsiderationsChange}
                />
            </div>
        </div>
    );
};

export default SelectConsiderations;
