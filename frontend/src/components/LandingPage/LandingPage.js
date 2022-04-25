import ListOfPlayers from "../ListOfPlayers/ListOfPlayers";
import PlayerStats from "../PlayerStats/PlayerStats";
import PositionsNeeded from "../PositionsNeeded/PositionsNeeded";
import RecommendedPlayers from "../RecommendedPlayers/RecommendedPlayers";
import TeamPicksMenu from "../TeamPicksMenu/TeamPicksMenu";
import TeamStats from "../TeamStats/TeamStats";
import "./LandingPage.css";
import draft from "../../data/draft.json"
import axios from "axios"
import { useEffect, useState } from "react";


function LandingPage() {
    return (
        <div className="landing-page">
            <div className="team-picks-menu">
                <TeamPicksMenu/>
            </div>
            <div className="middle">
                <div className="positions-needed side-by-side">
                    <PositionsNeeded/>
                </div>
                <div className="stats side-by-side">
                    <div className="stats-row">
                        <TeamStats/>
                    </div>
                    <div className="stats-row">
                        <PlayerStats />
                    </div>
                </div>
                <div className="recommended-players side-by-side">
                    <RecommendedPlayers />
                </div>
            </div>
            <div className="list-of-players">
                <ListOfPlayers />
            </div>
        </div>
    );
}

export default LandingPage;