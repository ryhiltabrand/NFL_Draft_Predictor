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
    var [draftees, setDraftees] = useState([]);
    const host = window.location.hostname;
    const port = 8000;
    var [increment, setIncrement] = useState(0)

    useEffect(() => {
        setTeam(draft[increment]);
        setLoaded(true);
        axios.get(`http://${host}:${port}/api/Drafted/?format=json`).then((res)=>{
                setDraftees(res.data);
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
                </div>
                <div className="recommended-players side-by-side">
                    <RecommendedPlayers team={team}/>
                </div>
            </div>
            <div className="list-of-players">
                <ListOfPlayers team={team} draftees={draftees} setDraftees={setDraftees}
                setTeam={setTeam} increment={increment} setIncrement={setIncrement}/>
            </div>
        </div> : ""}
        </>
    );
}

export default LandingPage;