import React, { useState, useEffect } from "react";
import {
  AppBar,
  Tabs,
  Tab,
  Toolbar,
  Button,
  Menu,
  MenuItem,
  SwipeableDrawer,
  IconButton,
  List,
  ListItem,
  ListItemText,
} from "@material-ui/core";
import useScrollTrigger from "@material-ui/core/useScrollTrigger";
import { makeStyles } from "@material-ui/styles";
import { Link } from "react-router-dom";
import useMediaQuery from "@material-ui/core/useMediaQuery"; // https://v4.mui.com/components/use-media-query/
import { useTheme } from "@material-ui/core/styles";
import MenuIcon from "@material-ui/icons/Menu";

import logo from "../../assets/logo.svg";

function ElevationScroll(props) {
  const { children } = props;

  const trigger = useScrollTrigger({
    disableHysteresis: true,
    threshold: 0, // koliko ce da ceka dok user skroluje da se pojavi efekat
  });

  return React.cloneElement(children, {
    elevation: trigger ? 4 : 0,
  });
}

const useStyles = makeStyles((theme) => ({
  toolbarMargin: {
    ...theme.mixins.toolbar,
    marginBottom: "3em",
    [theme.breakpoints.down("md")]: {
      marginBottom: "2em",
    },
    [theme.breakpoints.down("xs")]: {
      marginBottom: "1.25em",
    },
  },
  logo: {
    height: "8em",
    [theme.breakpoints.down("md")]: {
      height: "7em",
    },
    [theme.breakpoints.down("xs")]: {
      height: "5.5em",
    },
  },
  logoContainer: {
    padding: 0,
    "&:hover": {
      backgroundColor: "transparent", // ovim se opacity brise
    },
  },
  tabContainer: {
    marginLeft: "auto",
  },
  tab: {
    ...theme.typography.tab, // ovo je spread styles koji se nalazi u fajlu Theme
    minWidth: 10,
    marginLeft: "25px",
  },
  button: {
    ...theme.typography.estimate,
    borderRadius: "50px",
    marginLeft: "50px",
    marginRight: "50px",
    height: "45px",
    "&:hover": {
      backgroundColor: theme.palette.secondary.light,
    },
  },
  menu: {
    backgroundColor: theme.palette.common.blue,
    color: "white",
    borderRadius: "0px", // ovako se postize da ivice budu ostre u popup meniju
  },
  menuItem: {
    ...theme.typography.tab,
    opacity: 0.7,
    "&:hover": {
      opacity: 1,
    },
  },
  drawerIcon: {
    height: "50px",
    width: "50px",
  },
  drawerIconContainer: {
    marginLeft: "auto",
    "&:hover": {
      backgroundColor: "transparent",
    },
  },
  drawer: {
    backgroundColor: theme.palette.common.blue,
  },
  drawerItem: {
    ...theme.typography.tab,
    color: "white",
    opacity: 0.7,
  },
  drawerItemEstimate: {
    backgroundColor: theme.palette.common.orange,
  },
  drawerItemSelected: {
    "& .MuiListItemText-root": {
      // iz dokumentacije
      opacity: 1,
    },
  },
  appbar: {
    zIndex: theme.zIndex.modal + 1, // iz dokumentacije
  },
}));

export default function Header({
  value,
  setValue,
  selectedIndex,
  setSelectedIndex,
}) {
  const classes = useStyles();
  const theme = useTheme(); // koriscenje theme kroz varijablu, ne kroz funkciju, kako bi se mogli menjati parametri
  const iOS = process.browser && /iPad|iPhone|iPod/.test(navigator.userAgent); // proverava se da li je IOS

  const matches = useMediaQuery(theme.breakpoints.down("md"));

  const [openDrawer, setOpenDrawer] = useState(false);
  const [anchorEl, setAnchorEl] = useState(null);
  const [open, setOpen] = useState(false);

  const handleChange = (e, newValue) => {
    setValue(newValue);
  };

  const handleOpen = (e) => {
    setAnchorEl(e.currentTarget); // ovo je trenutna pozicija gde se klikce
    setOpen(true);
  };

  const handleClose = (e) => {
    setAnchorEl(null);
    setOpen(false);
  };

  const handleMenuItemClick = (e, i) => {
    setAnchorEl(null);
    setOpen(false);
    setSelectedIndex(i);
  };

  const menuOptions = [
    { name: "Services", link: "/services", activeIndex: 1, selectedIndex: 0 },
    {
      name: "Custom Software Development",
      link: "/customsoftware",
      activeIndex: 1,
      selectedIndex: 1,
    },
    {
      name: "Mobile App Development",
      link: "/mobileapps",
      activeIndex: 1,
      selectedIndex: 2,
    },
    {
      name: "Website Development",
      link: "/websites",
      activeIndex: 1,
      selectedIndex: 3,
    },
  ];

  const routes = [
    { name: "Home", link: "/", activeIndex: 0 },
    {
      name: "Services",
      link: "/services",
      activeIndex: 1,
      ariaOwns: anchorEl ? "simple-menu" : undefined,
      ariaPopup: anchorEl ? "true" : undefined,
      mouseOver: (event) => handleOpen(event),
    },
    { name: "The Revolution", link: "/revolution", activeIndex: 2 },
    { name: "About Us", link: "/about", activeIndex: 3 },
    { name: "Contact Us", link: "/contact", activeIndex: 4 },
  ];

  // useEffect(() => {
  //   // if (window.location.pathname === "/" && value !== 0) {
  //   //   setValue(0);
  //   // } else if (window.location.pathname === "/services" && value !== 1) {
  //   //   setValue(1);
  //   // } else if (window.location.pathname === "/revolution" && value !== 2) {
  //   //   setValue(2);
  //   // } else if (window.location.pathname === "/about" && value !== 3) {
  //   //   setValue(3);
  //   // } else if (window.location.pathname === "/contact" && value !== 4) {
  //   //   setValue(4);
  //   // } else if (window.location.pathname === "/estimate" && value !== 5) {
  //   //   setValue(5);
  //   // } ili sa ovim dole, na isto dodje

  //   switch (window.location.pathname) {
  //     case "/":
  //       if (value !== 0) {
  //         setValue(0);
  //       }
  //       break;
  //     case "/services":
  //       if (value !== 1) {
  //         setValue(1);
  //         setSelectedIndex(0);
  //       }
  //       break;
  //     case "/customsoftware":
  //       if (value !== 1) {
  //         setValue(1);
  //         setSelectedIndex(1);
  //       }
  //       break;
  //     case "/mobileapps":
  //       if (value !== 1) {
  //         setValue(1);
  //         setSelectedIndex(2);
  //       }
  //       break;
  //     case "/websites":
  //       if (value !== 1) {
  //         setValue(1);
  //         setSelectedIndex(3);
  //       }
  //       break;
  //     case "/revolution":
  //       if (value !== 2) {
  //         setValue(2);
  //       }
  //       break;
  //     case "/about":
  //       if (value !== 3) {
  //         setValue(3);
  //       }
  //       break;
  //     case "/contact":
  //       if (value !== 4) {
  //         setValue(4);
  //       }
  //       break;
  //     case "/estimate":
  //       if (value !== 5) {
  //         setValue(5);
  //       }
  //       break;
  //     default:
  //       break;
  //   }
  // }, [value]); bolje je ovo dole

  useEffect(() => {
    [...menuOptions, ...routes].forEach((route) => {
      switch (window.location.pathname) {
        case `${route.link}`:
          if (value !== route.activeIndex) {
            setValue(route.activeIndex);
            if (route.selectedIndex && route.selectedIndex !== selectedIndex) {
              setSelectedIndex(route.selectedIndex);
            }
          }
          break;
        case "/estimate":
          setValue(5);
          break;
        default:
          break;
      }
    });
  }, [value, menuOptions, selectedIndex, routes, setValue, setSelectedIndex]);

  const tabs = (
    <React.Fragment>
      <Tabs
        value={value}
        onChange={handleChange}
        className={classes.tabContainer}
        indicatorColor="primary"
      >
        {routes.map((route, index) => (
          <Tab
            key={`${route}${index}`}
            className={classes.tab}
            component={Link}
            to={route.link}
            label={route.name}
            aria-owns={route.ariaOwns}
            aria-haspopup={route.ariaPopup}
            onMouseOver={route.mouseOver}
          />
        ))}
      </Tabs>
      <Button
        component={Link}
        to="/estimate"
        variant="contained"
        color="secondary"
        className={classes.button}
        onClick={() => setValue(5)}
      >
        Free Estimate
      </Button>
      <Menu
        id="simple-menu"
        anchorEl={anchorEl}
        open={open}
        onClose={handleClose}
        classes={{ paper: classes.menu }} // classes je iz dokumentacije, kao i paper
        MenuListProps={{
          onMouseLeave: handleClose, // iz dokumentacije mui MenuListProps
        }}
        elevation={0}
        style={{ zIndex: 1302 }}
        keepMounted // za search engine
      >
        {menuOptions.map((option, i) => (
          <MenuItem
            key={`${option}${i}`}
            component={Link}
            to={option.link}
            classes={{ root: classes.menuItem }}
            onClick={(event) => {
              handleMenuItemClick(event, i);
              setValue(1);
              handleClose();
            }}
            selected={i === selectedIndex && value === 1}
          >
            {option.name}
          </MenuItem>
        ))}
      </Menu>
    </React.Fragment>
  );

  const drawer = (
    <React.Fragment>
      <SwipeableDrawer
        disableBackdropTransition={!iOS} // za mobile performance
        disableDiscovery={iOS} // za mobile performance
        open={openDrawer}
        onClose={() => setOpenDrawer(false)}
        onOpen={() => setOpenDrawer(true)}
        classes={{ paper: classes.drawer }}
      >
        <div className={classes.toolbarMargin} />
        <List disablePadding>
          {routes.map((route) => (
            <ListItem
              divider
              key={`${route}${route.activeIndex}`}
              button
              component={Link}
              to={route.link}
              selected={value === route.activeIndex}
              classes={{ selected: classes.drawerItemSelected }}
              onClick={() => {
                setOpenDrawer(false);
                setValue(route.activeIndex);
              }}
            >
              <ListItemText className={classes.drawerItem} disableTypography>
                {route.name}
              </ListItemText>
            </ListItem>
          ))}
          <ListItem
            onClick={() => {
              setOpenDrawer(false);
              setValue(5);
            }}
            divider
            button
            component={Link}
            classes={{
              root: classes.drawerItemEstimate,
              selected: classes.drawerItemSelected,
            }}
            to="/estimate"
            selected={value === 5}
          >
            <ListItemText className={classes.drawerItem} disableTypography>
              Free Estimate
            </ListItemText>
          </ListItem>
        </List>
      </SwipeableDrawer>
      <IconButton
        className={classes.drawerIconContainer}
        onClick={() => setOpenDrawer(!openDrawer)}
        disableRipple
      >
        <MenuIcon className={classes.drawerIcon} />
      </IconButton>
    </React.Fragment>
  );

  return (
    // sa Toolbar komponenta iz mui, se stavlja sve u horizontalnu liniju, position fixed je default, ima i static (onda ima margine sa strana)
    // color primary je default, sto dobija iz theme varijable
    <React.Fragment>
      <ElevationScroll>
        <AppBar position="fixed" className={classes.appbar}>
          <Toolbar disableGutters>
            <Button
              component={Link}
              to="/"
              className={classes.logoContainer}
              onClick={() => setValue(0)}
              disableRipple // ripple je efekat
            >
              <img alt="company logo" src={logo} className={classes.logo} />
            </Button>
            {matches ? drawer : tabs}
          </Toolbar>
        </AppBar>
      </ElevationScroll>
      <div className={classes.toolbarMargin} />
    </React.Fragment>
  );
}
