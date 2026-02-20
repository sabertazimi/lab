use git2::{Commit, Error, ObjectType, Repository};

pub trait GetHeadCommit {
    fn get_head_commit(&self) -> Result<Commit<'_>, Error>;
}

impl GetHeadCommit for Repository {
    fn get_head_commit(&self) -> Result<Commit<'_>, Error> {
        let obj = self.head()?.resolve()?.peel(ObjectType::Commit)?;
        obj.into_commit()
            .map_err(|_| Error::from_str("Couldn't find commit!"))
    }
}
