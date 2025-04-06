import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Logo from "../Assets/greentrip.svg";
import {
  Box,
  Drawer,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  List,
} from "@mui/material";
import HomeIcon from "@mui/icons-material/Home";
import InfoIcon from "@mui/icons-material/Info";
import LoginIcon from "@mui/icons-material/Login";
import MenuBookIcon from "@mui/icons-material/MenuBook";
import DashboardIcon from "@mui/icons-material/Dashboard";
import AirplaneTicketIcon from "@mui/icons-material/AirplaneTicket";
import AccountBoxIcon from "@mui/icons-material/AccountBox";
import { HiOutlineBars3 } from "react-icons/hi2";

const Navbar = () => {
  const [token, setToken] = useState(sessionStorage.getItem("token"));

  const [openMenu, setOpenMenu] = useState(false);

  const baseMenu = [
    {
      text: "Home",
      icon: <HomeIcon />,
      link: "/",
    },
    {
      text: "About us",
      icon: <InfoIcon />,
      link: "/info",
    },
    {
      text: "Book",
      icon: <MenuBookIcon />,
      link: "/magazine",
    },
    {
      text: "Planner",
      icon: <AirplaneTicketIcon />,
      link: "/travelplanner",
    },
    {
      text: "Dashboard",
      icon: <DashboardIcon />,
      link: "/dashboard",
    },
  ];
  const [menuOptions, setMenuOptions] = useState(baseMenu);

  useEffect(() => {
    const storedToken = sessionStorage.getItem("token");
    setToken(storedToken);

    const updatedMenu = [
      ...baseMenu,
      storedToken
        ? {
            text: "Profile",
            icon: <AccountBoxIcon />,
            link: "/profile",
          }
        : {
            text: "Login",
            icon: <LoginIcon />,
            link: "/login",
          },
    ];

    setMenuOptions(updatedMenu);
  }, [token]);

  return (
    <nav
      className="flex items-center justify-between min-h-[80px] max-h-[15vh] shadow-sm hover:shadow-xl 
    bg-tea-green rounded-xl mt-4 mx-5"
    >
      <div className="nav-logo-container mt-2.5 ml-5 mb-2.5 max-w-[200px]">
        <Link to="/">
          <img src={Logo} alt="GreenTrip logo" />
        </Link>
      </div>

      <div className="navbar-links-container space-x-12 no-underline text-black text-lg mr-6">
        <Link className="navbar-link" to="/">
          Home
        </Link>
        <Link className="navbar-link" to="/info">
          Info
        </Link>
        <Link className="navbar-link" to="/magazine">
          Book
        </Link>
        <Link className="navbar-link" to="/travelplanner">
          Planner
        </Link>
        <Link className="navbar-link" to="/dashboard">
          Dashboard
        </Link>
        {token ? (
          <Link className="button-link" to="/profile">
            <button
              className="px-7 py-3.5 bg-emerald hover:bg-green-600 text-black outline-none border-none rounded-[5rem] text-lg
        font-thin cursor-pointer transition duration-200 hover:shadow-2xl shadow-sm"
            >
              Profile
            </button>
          </Link>
        ) : (
          <Link className="button-link" to="/login">
            <button
              className="px-7 py-3.5 bg-emerald hover:bg-green-600 text-black outline-none border-none rounded-[5rem] text-lg
          font-thin cursor-pointer transition duration-200 hover:shadow-2xl shadow-sm"
            >
              Login
            </button>
          </Link>
        )}
      </div>

      <div className="navbar-menu-container">
        <HiOutlineBars3 onClick={() => setOpenMenu(true)} />
      </div>
      <Drawer open={openMenu} onClose={() => setOpenMenu(false)} anchor="right">
        <Box
          width="50vw"
          role="presentation"
          onClick={() => setOpenMenu(false)}
          onkeyDown={() => setOpenMenu(false)}
        >
          <List style={{ width: "100%" }}>
            {menuOptions.map((item) => (
              <ListItem key={item.text} disablePadding>
                <Link to={item.link} className="navbar-link">
                  <ListItemButton
                    style={{ width: "100%" }}
                    sx={{ alignItems: "center" }}
                  >
                    <ListItemIcon>{item.icon}</ListItemIcon>
                    <ListItemText
                      primary={item.text}
                      sx={{ fontSize: "20px !important" }}
                    />
                  </ListItemButton>
                </Link>
              </ListItem>
            ))}
          </List>
        </Box>
      </Drawer>
    </nav>
  );
};

export default Navbar;
