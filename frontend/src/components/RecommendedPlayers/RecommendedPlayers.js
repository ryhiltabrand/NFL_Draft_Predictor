import axios from "axios"
import { useEffect, useState } from "react";
import Card from "react-bootstrap/Card";

function RecommendedPlayers(props) {

    var team = props.team;
    const host = window.location.hostname;
    const port = 8000;

    const [players, setPlayers] = useState([]);
    const [loaded, setLoaded] = useState(false);

    useEffect(() => {
        axios.get(`http://${host}:${port}/rec/${team.acryonm}`).then((res) => {
            setPlayers(res.data)
            setLoaded(true);
            console.log(true)
        })
    }, []);

    return (
        <div>
            Recommended Players
            {
                loaded ? players.map((player) =>
                    <div>
                        Name: {player.name} Height: {player.height} Position: {player.position} Position Grade: {player.positionGrade}
                    </div>
                ) : ""
            }
        </div>
    );
}

export default RecommendedPlayers;