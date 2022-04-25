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

    var [team, setTeam] = useState({});
    var [loaded, setLoaded] = useState(false);

    useEffect(() => {
        const teams = Object.values(draft);
        const randTeam = teams[parseInt(Math.random() * teams.length)]
        setTeam(randTeam);
        setLoaded(true);
        
    }, []);

    return (
        <>

       { loaded ? <div className="landing-page">
            <div className="team-picks-menu">
                <TeamPicksMenu team={team}/>
            </div>
            <div className="middle">
                <div className="positions-needed side-by-side">
                    <PositionsNeeded team={team}/>
                </div>
                <div className="stats side-by-side">
                    <div className="stats-row">
                        <TeamStats team={team}/>
                    </div>
                    <div className="stats-row">
                        <PlayerStats team={team}/>
                    </div>
                </div>
                <div className="recommended-players side-by-side">
                    <RecommendedPlayers team={team}/>
                </div>
            </div>
            <div className="list-of-players">
                <ListOfPlayers team={team}/>
            </div>
        </div> : ""}
        </>
    );
}

export default LandingPage;