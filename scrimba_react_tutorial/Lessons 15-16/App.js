import React from "react"

import Header from "./components/Header"
import MainContent from "./components/MainContent"
import Footer from "./components/Footer"
import Time from "./components/Time"

function App() {
    return (
        <div>
            <Header />
            <Time />
            <MainContent />
            <Footer />
        </div>
    )
}

export default App