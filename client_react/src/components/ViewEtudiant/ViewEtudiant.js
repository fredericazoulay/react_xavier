import React, { Component } from 'react'
import axios from 'axios'
import { API_URL } from '../../config';

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { confirmAlert } from 'react-confirm-alert';
import 'react-confirm-alert/src/react-confirm-alert.css'

export default class ViewEtudiant extends Component {
    constructor(props) {
        super(props)
        this.viewStudent = this.viewStudent.bind(this)
    }

    async viewStudent() {
        console.log('view' + this.props.etudiant.id_etudiant)
        //await axios.delete(`${API_URL}/etudiant/${this.props.etudiant.id_etudiant}`)

        this.render2();
    }

    render() {
        return(
            <button onClick={this.viewStudent}>
                View
            </button>
        )
    }



    render2() {

        return (
            <div className="form-horizontal pad-10">
                <ToastContainer />
                <div className="h2 text-center">View Etudiant</div>
                <br/>

                    <div className="col-md-6 form-group">
                        <label htmlFor="matricule" className="control-label">Matricule</label>
                        <div className="col-md-12 no-padding">
                            <input value={this.props.etudiant.matricule} name="matricule" id="matricule" className="form-control" placeholder="" type="text" required />
                        </div>
                    </div>
                    <div className="col-md-6 form-group">
                        <label htmlFor="nom"  className="control-label">Nom</label>
                        <div className="col-md-12 no-padding">
                            <input name="nom" value={this.props.etudiant.nom} id="nom" className="form-control" placeholder="" type="text" required />
                        </div>
                    </div>
                    <div className="col-md-6 form-group">
                        <label htmlFor="prenom"  className="control-label">Prénom</label>
                        <div className="col-md-12 no-padding">
                            <input name="prenom" value={this.props.etudiant.prenom} id="prenom" className="form-control" placeholder="" type="text" required />
                        </div>
                    </div>
                    <div className="col-md-12">
                        <div>
                            <button type="submit" className="btn btn-save btn-primary">Back
                            </button>
                        </div>
                    </div>
                
            </div>

        )
    }


    
}