import React from "react";
import { createBrowserRouter } from "react-router-dom";
import MainDashBoardComp from "../Components/MainDashBoardComp";
import AboutComp from "../Components/AboutComp";
import ContactsComp from "../Components/ContactComps";
import ProductsComp from "../Components/ProductComp";



const routing=createBrowserRouter([
    {path:"",element:<MainDashBoardComp/>},
    {path:"about",element:<AboutComp/>},
    {path:"contacts",element:<ContactsComp/>},
    {path:"products",element:<ProductsComp/>}
])

export default routing;