import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import Logo from '../Assets/docGPTAltLogo.svg';
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
    <nav>
      <div className="nav-logo-container">
        <Link to="/">
          <img src={Logo} alt="DocGPT" />
        </Link>
      </div>
      <div className="navbar-links-container">
        <Link to="/" className="navbar-link">Home</Link>
        <Link to="/info" className="navbar-link">Info</Link>
        <Link to="/magazine" className="navbar-link">Book</Link>
        <Link to="/travelplanner" className="navbar-link">Planner</Link>
        <Link to="/login" className="button-link">
          <button className="primary-button">
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