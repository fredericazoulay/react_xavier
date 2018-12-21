import React from 'react';
import './TableEtudiants.css';
import PropTypes from 'prop-types';
import {withRouter} from 'react-router-dom';
import DeleteEtudiant from '../../DeleteEtudiant/DeleteEtudiant.js';
import UpdateEtudiant from '../../UpdateEtudiant/UpdateEtudiant.js';
import ViewEtudiant from '../../ViewEtudiant/ViewEtudiant.js';


class TableEtudiants extends React.Component 
{

    constructor(props) 
    {
        super(props);
        this.state = { edit: false,
            matricule:'zz',
            nom:'zz',
            prenom:'zzz'
        };

        /*
        this.setState({
            edit: false,
            matricule:'',
            nom:'',
            prenom:''
        })
        */

        this.etudiants = this.props.etudiants
    }

    edit() {
        this.edit = !this.edit
    }

    update()
    {
        console.log("UPDATE_matricule:" + this.state.matricule);
        console.log("UPDATE_nom:" + this.state.nom);
        console.log("UPDATE_prenom:" + this.state.prenom);

        /*
        this.newetudiant = {
            edit: 'true',
            matricule: this.state.matricule,
            nom: this.state.nom,
            prenom: this.state.prenom
        }
        */

        this.state.newetudiant = { edit: false,
            matricule: this.state.matricule,
            nom: this.state.nom,
            prenom: this.state.prenom
        };

        //this.props.newetudiant = this.state.newetudiant;
        console.log("UPDATE_newetudiant:" + this.state.newetudiant);
    }

    render() 
    {

    //const TableEtudiants = (props) => {
        //const {etudiants, history} = props;
        //const {etudiants, history, rerender} = props;

        if(this.edit == false)
        {

        }
        else
        {

        }

        return (<div className="table-container">
            <div className="h2 text-center">Liste Etudiant</div>
            <div className="row">
                <div className="col-md-12 pad-10">
                    <button onClick={()=> this.props.history.push(`/ajout`)} type="submit" className="btn btn-primary">
                        Ajout Etudiant
                    </button>
                </div>
            </div>
            <br/>
            <br/>
            <table className="table table-striped">
                <thead className="Table-head">
                <tr>
                    <th>Matricule</th>
                    <th>Nom</th>
                    <th>Prenom</th>
                    <th>DeleteEtudiant</th>
                    <th>ViewEtudiant</th>
                    <th>UpdateEtudiant</th>
                </tr>
                </thead>
                <tbody>
                {this.props.etudiants.map((etudiant) => (
                    <tr key={etudiant.id_etudiant}
                    >

                        <td>
                            <span>{etudiant.matricule}</span>
                        </td>
                        <td>
                            <span>{etudiant.nom}</span>
                        </td>
                        <td>
                            <span>{etudiant.prenom}</span>
                        </td>

                        
                        <td>
                        <span><input type="text" onChange={e => this.setState({ matricule: e.target.value }) } value={this.props.matricule} ></input></span>
                        </td>
                        <td>
                            <span><input type="text" onChange={e => this.setState({ nom: e.target.value }) } value={this.props.nom} ></input></span>
                        </td>
                        <td>
                            <span><input type="text" onChange={e => this.setState({ prenom: e.target.value }) } value={this.props.prenom} /></span>
                        </td>
                        

                        <td>
                            <span><DeleteEtudiant etudiant={etudiant} rerender={this.props.rerender} etudiants={this.props.etudiants}/></span>
                        </td>
                        <td>
                            <span><UpdateEtudiant onClick={this.update()} etudiant={etudiant} rerender={this.props.rerender} etudiants={this.props.etudiants} newetudiant={this.state.newetudiant}/></span>
                        </td>
                        <td>
                            <span> <ViewEtudiant etudiant={etudiant} rerender={this.props.rerender} etudiants={this.props.etudiants}/> </span>
                        </td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>)
    }


}

TableEtudiants.propTypes = 
{
    etudiants: PropTypes.array.isRequired,
}

// <span><DeleteEtudiant etudiant={etudiant} rerender={rerender} /></span>

//componentDidUpdate() {
    //this.fetchEtudiants();
//}

export default withRouter(TableEtudiants);

//async deleteLocalStudent() {
//    students.splice(students.indexOf(student), 1)
//}