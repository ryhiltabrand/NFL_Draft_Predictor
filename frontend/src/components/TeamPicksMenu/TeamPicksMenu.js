import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import { ImageListItemBar, Typography } from '@mui/material';
import Card from '@mui/material/Card';
import CardActionArea from '@mui/material/CardActionArea';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import { useEffect, useState } from "react";
import axios from "axios";
import ScrollMenu from 'react-horizontal-scroll-menu';
import "./TeamPicksMenu.css";

function TeamPick(teamName, pickNumber) {

    return (
        <CardActionArea component='a' href='#'>
            <Card sx={{display: 'flex'}}>
                <CardContent sx={{flex:1}}>
                    <Typography component="h2" variant="h5">
                        {`Pick ${pickNumber}:`}
                    </Typography>
                    <Typography variant="subtitle1" paragraph>
                        {teamName}
                    </Typography>
                </CardContent>
            </Card>
        </CardActionArea>
    )
}

function TeamPicksMenu() {

    const [teams, setTeams] = useState([]);

    useEffect(() => {
        axios.get("http://localhost:8000/api/Team/?format=json").then((res) => {
            setTeams(res.data)
        });
    }, []);

    var teamPicks = teams.map((team, pickNumber) =>
        <div style={{ display: "inline-block" }}>
            {TeamPick(team.name, pickNumber + 1)}
        </div>
    );

    // console.log(teamPicks)

    return (
        //<div>Scrollable List</div>
        <ScrollMenu
            data={teamPicks}
            dragging={false}
        />
    );
}

export default TeamPicksMenu;