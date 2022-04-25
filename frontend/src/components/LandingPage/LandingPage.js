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
    const [players, setPlayers] = useState([]);

    var teamIndex = 0;
    const host = window.location.hostname;
    const port = 8000;

    useEffect(() => { 
        setTeam(draft[teamIndex]);
        setLoaded(true)

        axios.get(`http://${host}:${port}/rec/${team.acryonm}`).then((res) => {
            setPlayers(res.data)
            setLoaded(true);
        })
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
                    <RecommendedPlayers players={players}/>
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