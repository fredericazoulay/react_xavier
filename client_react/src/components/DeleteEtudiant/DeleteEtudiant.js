import React, { Component } from 'react'
import axios from 'axios'
import { API_URL } from '../../config';

export default class DeleteEtudiant extends Component {
    constructor(props) {
        super(props)
        this.deleteStudent = this.deleteStudent.bind(this)
    }

    async deleteStudent() {
        console.log('delete' + this.props.etudiant.id_etudiant)
        await axios.delete(`${API_URL}/etudiant/${this.props.etudiant.id_etudiant}`)

        console.log(this.props.etudiants);

        this.props.rerender(this.props.etudiants, this.props.etudiant);
        //componentDidUpdate() ;
    }

    render() {
        return(
            <button onClick={this.deleteStudent}>
                Delete
            </button>
        )
    }



    refreshEtudiant() 
    {
        /*
        let data = {
            "matricule": this.state.matricule,
            "nom": this.state.nom,
            "prenom": this.state.prenom
        };
        */

        fetch(`${API_URL}/etudiant`, {
            method: 'post',
            headers: {'Accept': 'application/json', 'Content-Type': 'application/json',},
            body: ''//JSON.stringify(data)
        }).then((result) => {
            console.log(result);
            this.notify();
            this.props.history.push('/');
        }).catch((err) => {
            console.log(err);
        });
    }

    componentDidUpdate() 
    {
        console.log("componentDidUpdate");
    //this.fetchEtudiants();
    }

}