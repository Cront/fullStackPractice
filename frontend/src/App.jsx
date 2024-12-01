import { useState, useEffect } from 'react'
import ContactList from './ContactList'
import ContactForm from './ContactForm'
import './App.css'

function App() {
  // State to manage list of contacts
  const [contacts, setContacts] = useState([])
  // State to track whether the modal is open
  const [isModalOpen, setIsModalOpen] = useState(false)
  // State to track the current contact being edited
  const [currentContact, setCurrentContact] = useState({})

  // Fetch contacts on component mount
  useEffect(() => {
    fetchContacts()
  }, [])

  // Function to fetch contacts from the server
  const fetchContacts = async () => {
    const response = await fetch("http://127.0.0.1:5000/contacts")
    const data = await response.json()
    setContacts(data.contacts) // Set the contacts in state
    console.log(data.contacts)
  }

  // Function to close the modal
  const closeModal = () => {
    setIsModalOpen(false)
    setCurrentContact({})
  }

  // Function to open the modal for creating a new contact
  const openCreateModel = () => {
    if (!isModalOpen) setIsModalOpen(true)
  }

  // Function to open the modal for editing an existing contact
  const openEditModal = (contact) => {
    if (isModalOpen) return
    setCurrentContact(contact) // Set the selected contact in state
    setIsModalOpen(true)
  }

  // Callback to refresh contacts after update or creation
  const onUpdate = () => {
    closeModal()
    fetchContacts()
  }

  // Effect to handle closing the modal with the Escape key
  useEffect(() => {
    const handleKeyDown = (event) => {
      if (event.key === 'Escape') {
        closeModal()
      }
    }

    if (isModalOpen) {
      document.addEventListener('keydown', handleKeyDown)
    } else {
      document.removeEventListener('keydown', handleKeyDown)
    }

    return () => {
      document.removeEventListener('keydown', handleKeyDown)
    }
  }, [isModalOpen])

  return (
    <>
      {/* Pass contacts and functions to the ContactList component */}
      <ContactList contacts={contacts} updateContact={openEditModal} updateCallback={onUpdate}/> 
      <button onClick={openCreateModel}>Create New Contact</button>

      {/* Modal for creating or updating a contact */}
      {isModalOpen && <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={closeModal}>&times;</span>
            <ContactForm existingContact={currentContact} updateCallback={onUpdate} />
          </div>
        </div>
      }
    </>
  )
}

export default App
