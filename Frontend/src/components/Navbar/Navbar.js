import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import Logo from '../Assets/logoipsum-215.svg';
import { Box, Drawer, ListItem, ListItemButton, ListItemIcon, ListItemText, List } from "@mui/material";
import HomeIcon from "@mui/icons-material/Home";
import InfoIcon from "@mui/icons-material/Info";
import { HiOutlineBars3 } from "react-icons/hi2";

const Navbar = () => {
  const [openMenu, setOpenMenu] = useState(false)
  const menuOptions = [
    {
      text: "Home",
      icon: <HomeIcon />,
      link: "/"
    },
    {
      text: "About us",
      icon: <InfoIcon />,
      link: "/info"
    },
    {
      text: "Login",
      icon: <InfoIcon />,
      link: "/login"
    }
  ];

  return (
    <nav className="flex items-center justify-between min-h-[90px] max-h-[10vh] shadow-sm hover:shadow-xl 
    bg-tea-green rounded-xl mt-4 mx-5">

      <div className="mt-2.5 ml-5 mb-2.5 max-w-[200px]">
        <Link to="/">
          <img src={Logo} alt="GreenTrip logo" />
        </Link>
      </div>

      <div className="space-x-12 no-underline text-black text-xl mr-6">
        <Link to="/">Home</Link>
        <Link to="/info">Info</Link>
        <Link to="/magazine">Book</Link>
        <Link to="/travelplanner">Planner</Link>
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/login">
          <button className="px-7 py-3.5 bg-emerald text-black outline-none border-none rounded-[5rem] text-xl
          font-thin cursor-pointer transition duration-200 hover:shadow-2xl shadow-sm">
            Login
          </button>
        </Link>
      </div>

      <div className="navbar-menu-container">
        <HiOutlineBars3 onClick={() => setOpenMenu(true)} />
      </div>
      <Drawer open={openMenu} onClose={() => setOpenMenu(false)} anchor="right"  >
        <Box
          width="50vw"
          role="presentation"
          onClick={() => setOpenMenu(false)}
          onkeyDown={() => setOpenMenu(false)}
        >
          <List style={{ width: '100%' }}>
            {menuOptions.map((item) => (
              <ListItem key={item.text} disablePadding >
                <Link to={item.link} className="navbar-link">
                <ListItemButton style={{ width: '100%' }} sx={{ alignItems: 'center' }}>
                  <ListItemIcon>
                    {item.icon}
                  </ListItemIcon>
                  <ListItemText primary={item.text} sx={{ fontSize: '20px !important' }} />
                </ListItemButton>
                </Link>
              </ListItem>
            ))}
          </List>
        </Box>
      </Drawer>
    </nav >
  )
}

export default Navbar