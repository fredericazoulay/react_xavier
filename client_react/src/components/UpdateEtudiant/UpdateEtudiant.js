import React, { Component } from 'react'
import axios from 'axios'
import { API_URL } from '../../config';

export default class UpdateEtudiant extends Component {
    constructor(props) {
        super(props)
        this.updateStudent = this.updateStudent.bind(this)
    }

    async updateStudent() {
        console.log('update' + this.props.etudiant.id_etudiant)

        let data = {
            matricule: this.props.newetudiant.matricule,
            nom: this.props.newetudiant.nom,
            prenom: this.props.newetudiant.prenom
        };

        //let newEtudiant = this.props.newetudiant;
        await axios.put(`${API_URL}/etudiant/${this.props.etudiant.id_etudiant}`, data)
    }

    update() {

    }

    render() {
        return(
            <button onClick={this.updateStudent}>
                Update
            </button>
        )
    }

    
}